/*
 * (C) Copyright 2006-2016 Nuxeo SA (http://nuxeo.com/) and others.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Contributors:
 *     Tiago Cardoso <tcardoso@nuxeo.com>
 */
package org.nuxeo.ecm.platform.threed.service;

import org.nuxeo.ecm.core.api.Blob;
import org.nuxeo.ecm.core.api.DocumentModel;
import org.nuxeo.ecm.platform.threed.ThreeD;
import org.nuxeo.ecm.platform.threed.TransmissionThreeD;

import java.util.Collection;

/**
 * Service to asynchronously launch and monitor 3D format conversions (including lod) and rendering.
 *
 * @since 8.4
 */
public interface ThreeDService {

    /**
     * Launch all the registered automatic lod transmission version and thumbnail render on the given {@code doc}.
     *
     * @param doc the 3D document to be converted
     */
    void launchBatchConversion(DocumentModel doc);

    /**
     * Batch convert the {@code originalThreed} to all needed blobs (lod transmission formats and thumbnail render)
     *
     * @param originalThreed the 3d to convert
     * @return a {@code List<Blob>} object of the converted assets.
     */
    Collection<Blob> batchConvert(ThreeD originalThreed);

    /**
     * Batch convert the Collada {@code colladaThreeD} to glTF
     *
     * @param colladaThreeD the 3d to convert
     * @return a {@code TransmissionThreeD} object of in glTF.
     */
    TransmissionThreeD convertColladaToglTF(TransmissionThreeD colladaThreeD);

    /**
     * Returns the available registered render views on a 3D content.
     */
    Collection<RenderView> getAvailableRenderViews();

    /**
     * Returns the available registered automatic LODs on a 3D content.
     */
    Collection<AutomaticLOD> getAutomaticLODs();

    /**
     * Returns the available registered Automatic LOD by percentage.
     */
    AutomaticLOD getAutomaticLOD(int percentage);

    /**
     * Returns the available registered render views by name.
     */
    RenderView getRenderView(String renderViewName);

    /**
     * Returns the available registered render views by azimuth and zenith (the combination is always unique).
     */
    RenderView getRenderView(Integer azimuth, Integer Zenith);

}
